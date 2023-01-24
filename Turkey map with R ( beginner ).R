#Türkiye haritasını yükle
library(rnaturalearth)
library(rnaturalearthdata)

# Türkiye haritasını çiz
world <- ne_countries(scale = "medium", returnclass = "sf")
turkey <- world[world$iso_a3 == "TUR", ]
plot(turkey)