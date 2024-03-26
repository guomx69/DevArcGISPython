#1)install Anaconda  
#https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04
#Anaconda includes hundreds of packages, whereas Miniconda includes just a few. 
#conda is an open source tool that comes with both Anaconda and Miniconda, and it functions as both a package manager and an environment manager

curl https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh --output anaconda.sh &&\
sha256sum anaconda.sh &&\
bash anaconda.sh #conda update conda && conda update anaconda
conda -V

#2)setup python environment
#conda init bash && source ~/.bashrc
#conda config --set auto_activate_base True && conda config --set offline True && conda list && conda search "^python$"
 conda create --name ArcgisPython3.11 python=3.11  #conda remove --name my_env35 --allls
 #conda create --name my_env python=3 numpy
 conda activate ArcgisPython3.11 #python --version && conda deactivate && conda info --envs

#install package dotenv under ArcgisPython3.11 
conda install python-dotenv # if not work then use conda install conda-forge::python-dotenv

#3)install ArcGIS  
#https://developers.arcgis.com/python/guide/anaconda/
#https://developers.arcgis.com/python/guide/offline/
conda install -c esri arcgis #conda install -c esri arcgis --no-deps &&  pip install arcgis --no-deps

 #conda install anaconda-clean && anaconda-clean && rm -rf ~/anaconda3  && nano ~/.bashrc