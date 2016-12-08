BASE_URL="http://www.dis.uniroma1.it/challenge9/data/USA-road-d"

DIR=dimacs

echo 'Downloading DIMACS graphs'

for x in USA CTR W E LKS CAL NE NW FLA COL BAY NY; do
    wget "${BASE_URL}/USA-road-d.${x}.gr.gz" -P "${DIR}" # distance
#    wget "${BASE_URL}/USA-road-t.${x}.gr.gz" -P "${DIR}" # time
#    wget "${BASE_URL}/USA-road-d.${x}.co.gz" -P "${DIR}" # coordinates
done

echo 'Extracting graph files'

gunzip ${DIR}/*

echo 'Converting from DIMACS to "simple" format (this will take some time)'

sed -i -e '/^c/ d'        ${DIR}/*.gr
sed -i -e 's/^[^0-9]*//g' ${DIR}/*.gr
