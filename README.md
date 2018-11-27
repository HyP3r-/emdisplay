<h1>emdisplay</h1>
    <p>
        The emdisplay project can be used by fire brigades to receive incoming alarm faxes, display them graphically in
        the form of a web interface, forward them to the members and print them out.
    </p>
</div>

<h2 align="center">Install</h2>

Clone the repository and execute the install.sh:

```bash
git clone https://github.com/HyP3r-/emdisplay.git
cd emdisplay
sudo install.sh
```

<h2 align="center">Introduction</h2>

emdisplay consists of two components. A web interface which either visualises the current time and messages as well as
the status of the vehicles or evaluates the details of the alarmfax during an alarm and visualises them in the form of
a journey description as well as alarmed vehicles. In the background, a service is executed which receives the incoming
alarms, reads them, stores them for the website in the database and forwards them to the members of the fire brigade by
e-mail, SMS or instant message.
