mkdir -p ../atomics/gol
mkdir -p ../examples/gol
mkdir -p ../patterns
mkdir -p ../library/gol
mkdir -p ../output/gol

cp atomics/* ../atomics/gol
cp examples/* ../examples/gol
find patterns/* -type f -exec cp {} ../patterns \;
cp lib/* ../library/gol
cp logs/* ../output/gol

mv ../bin/powerdevs.ini ../bin/old_powerdevs.ini

cp powerdevs.ini ../bin
