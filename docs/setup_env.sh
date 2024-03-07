#1)install Anaconda
curl https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh --output anaconda.sh &&\
sha256sum anaconda.sh &&\
bash anaconda.sh

# source ~/.bashrc && conda list && conda search "^python$"
 conda create --name ArcgisPython3.11 python=3.11  #conda remove --name my_env35 --allls
 conda activate ArcgisPython3.11 #python --version && conda deactivate && conda info --envs