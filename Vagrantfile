Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  ## config.vm.network "private_network", ip: "192.168.33.10" #type: "dhcp"
  config.vm.network "private_network", type: "dhcp"
  ## config.vm.network "forwarded_port", guest: 5000, host: 8080
  config.vm.provision "shell", inline: <<-SHELL

    ## Installation de Python 3.9
    sudo apt-get update
    sudo apt-get install -y software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install -y python3.9

    ## Installation de venv
    sudo apt-get install -y python3.9-venv

    ## Création de l'environnement pour le TP2
    python3.9 -m venv /home/vagrant/inf5190_tp2_venv

    ## Création du répertoire où mettre les sources
    mkdir /vagrant/inf5190_tp2_src

    ## Installation de SQLite
    sudo apt-get install -y sqlite3
  SHELL
end

