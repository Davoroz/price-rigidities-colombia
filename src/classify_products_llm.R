# Classify product descriptions into CPI (COICOP) groups with a local LLM.
#
# Uses Llama 3 through Ollama (https://ollama.com) to assign each product
# description to one of the DANE consumer-price-index groups. The output was
# reviewed by hand and consolidated in data/product_classification.xlsx,
# which the tables (31) and figures (32) notebooks use.
#
# Requirements: a running Ollama server with the `llama3` model pulled, and
#   install.packages("devtools"); devtools::install_github("hauselin/ollamar")
# Run from the repository root.

library(ollamar)

wd <- "data/interim/"

# Ask the model to classify one product (prompt kept in Spanish, like the data)
classify_message_llama <- function(mensaje) {
  prompt <- paste0("Clasifica el siguiente producto en alguna de estos grupos:
  Alimentos y bebidas no alcohólicas
  Bebidas alcohólicas y tabaco
  Prendas de vestir y calzado
  Alojamiento, agua, electricidad, gas y otros combustibles
  Muebles, artículos para el hogar y conservación ordinaria de la vivienda
  Salud
  Transporte
  Información y comunicación
  Recreación y cultura
  Educación
  Restaurantes y hoteles
  Bienes y servicios diversos
  Asegurate de retornar unicamente el grupo en el cual clasificaste el producto: ", mensaje)

  response <- ollamar::generate(
    model = "llama3",
    prompt = prompt,
    output = "text"
  )
  return(response)
}

# Classify one batch of products
procesar_lote <- function(lote) {
  lote$clasificacion <- sapply(lote$descripcion, classify_message_llama)
  return(lote)
}

# Cleaned products of one retailer (output of the cleaning notebooks)
df <- read.csv(paste0(wd, "C_clean.csv"))

# Process in batches of 100 products
lote_tamano <- 100
lotes <- split(df, ceiling(seq_along(1:nrow(df)) / lote_tamano))
lotes_procesados <- lapply(lotes, procesar_lote)
df_clasificado <- do.call(rbind, lotes_procesados)

head(df_clasificado)

write.csv(df_clasificado, paste0(wd, "C_classified.csv"))

unique(df_clasificado$clasificacion)
