#!/bin/bash
#if you have installed conda, so no need to install docker image, just run command "jupyter notebook"
#because jupyter is installed by default,but it uses my local computer folder without the sample code


#docker pull ghcr.io/esri/arcgis-python-api-notebook

#docker run --name test_arcgis_python -it -p 8088:8888 ghcr.io/esri/arcgis-python-api-notebook
#docker run --name test_arcgis_python -it -p 8088:8888 ghcr.io/esri/arcgis-python-api-notebook bash
#docker run --entrypoint /bin/bash -it ghcr.io/esri/arcgis-python-api-notebook #https://www.warp.dev/terminus/docker-run-bash
#token: 214dac6f5aca9f13037c4d38759dd673b6aa5d2ddac95079 #sd

docker start test_arcgis_python

#docker exec -it test_arcgis_python /bin/bash #only when the contain is in running mode
#docker exec test_arcgis_python /bin/bash -c 'service ssh restart'