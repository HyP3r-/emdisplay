#!/usr/bin/env bash
# Install or Update Script for this Project
# Copyright (C) 2018  Andreas Fendt <mail@andreas-fendt.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# general:
# copy to install directory

# install system dependencies
apt update
apt install -y apache2 \
               mariadb-server mariadb-client libmariadbclient-dev \
               python3-wheel python3-venv python3-pip

# apache

# HylaFAX


# webserver:
# configure apache
# configure user rights

# service:
# install service (systemd)
