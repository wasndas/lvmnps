.. _actor-schema:

Actor schema
============

.. jsonschema::

    {
        "switches": {
            "DLI-NPS-01": {
                "type": "dli",
                "name": "LVM-PSU-01",
                "hostname": "10.7.45.22",
                "use_https": false,
                "user": "admin",
                "password": "rLXR3KxUqiCPGvA",
                "numports": 8,
                "ouo": false,
                "ports": {
                    "1": {
                        "name": "LVM-ARCHON-02",
                        "desc": "Archon controller"
                        },
                    "2": {
                        "name": "-",
                        "desc": ""
                        },
                    "3": {
                        "name": "Hg-Ar Lamp",
                        "desc": "spectral calibrationh lamp"
                        },
                    "4": {
                        "name": "MI-150 Light Source",
                        "desc": ""
                        },
                    "5": {
                        "name": "LVM IEB 02 (Spec Controller)",
                        "desc": "OSU spectrograph controller"
                        },
                    "6": {
                        "name": "LVM-ARCHON-01",
                        "desc": "Archon controller"
                        },
                    "7": {
                        "name": "625 nm LED (M625L4)",
                        "desc": "LED"
                        },
                    "8": {
                        "name": "LVM IEB 06 (Spec Controller) ",
                        "desc": "OSU spectrograph controller"
                        },
                    "num": 1
                }
            },
            "DLI-NPS-02": {
                "type": "dli",
                "name": "LVM-PSU-02",
                "hostname": "10.7.45.29",
                "use_https": false,
                "user": "admin",
                "password": "VCrht9wfx2CQN9b",
                "numports": 8,
                "ouo": false,
                "ports": {
                    "1": {
                        "name": "Router/Switch",
                        "desc": "Router power switch"
                        },
                    "2": {
                        "name": "Ln2 NIR valve",
                        "desc": "LVM Instrument Electronic Box"
                        },
                    "3": {
                        "name": "LVM-Archon-02",
                        "desc": ""
                        },
                    "4": {
                        "name": "IEB06",
                        "desc": "Archon controller"
                        },
                    "5": {
                        "name": null,
                        "desc": "Raspberry Pi PC"
                        },
                    "6": {
                        "name": "RPi",
                        "desc": "Cryogenic solenoid valve for liquid nitrogen."
                        },
                    "7": {
                        "name": "FFS LED",
                        "desc": ""
                        },
                    "8": {
                        "name": "Pressure transducers",
                        "desc": "Pressure transducers"
                        },
                    "num": 1
                }
            }
        },
        
        "timeouts": {
            "switch_connect": 3
            },
            
        "actor": {
            "name": "lvmnps",
            "host": "localhost",
            "port": 5672,
            "log_dir": "~/tmp/log"
            }
    }
