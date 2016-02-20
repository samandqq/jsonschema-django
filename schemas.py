json = {
    ###############
    "SwitchCreateListView.post": {
        ###############
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "configs": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "properties": {
                        "model": {
                            "type": "string",
                            "enum": [
                                "5900",
                                "6125xlg"
                            ]
                        },
                        "ip": {
                            "type": "string",
                            "oneOf": [
                                {
                                    "format": "ipv4"
                                }
                            ]
                        },
                        "num_ports": {
                            "type": "string",
                            "minLength": 1,
                            "default": "24"
                        },
                        "snmp": {
                            "type": "object",
                            "properties": {
                                "priv_mode": {
                                    "type": "string",
                                    "pattern": "^((SHA)|(DES))$"
                                },
                                "port": {
                                    "type": "string",
                                    "minLength": 1,
                                    "default": "161"
                                }
                            },
                            "required": [
                                "priv_mode",
                                "port"
                            ]
                        },
                        "netconf": {
                            "type": "object",
                            "properties": {
                                "user": {
                                    "type": "string",
                                    "minLength": 1,
                                    "default": "admin"
                                },
                                "port": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 1024,
                                    "exclusiveMaximum": True,
                                    "exclusiveMinimum": True
                                }
                            },
                            "required": [
                                "user",
                                "port"
                            ]
                        }
                    },
                    "required": [
                        "model",
                        "ip",
                        "num_ports",
                        "snmp",
                        "netconf"
                    ]

                }
            }
        },
        "required": [
            "configs"
        ]
    },
    ###############
    "GetUpdateDeleteView.put": {
        ###############
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "minItems": 1,
        "properties": {
            "model": {
                "type": "string",
                "enum": [
                    "5900",
                    "6125xlg"
                ]
            },
            "ip": {
                "type": "string",
                "oneOf": [
                    {
                        "format": "ipv4"
                    }
                ]
            },
            "num_ports": {
                "type": "string",
                "minLength": 1,
                "default": "24"
            },
            "snmp": {
                "type": "object",
                "properties": {
                    "priv_mode": {
                        "type": "string",
                        "pattern": "^((SHA)|(DES))$"
                    },
                    "port": {
                        "type": "string",
                        "minLength": 1,
                        "default": "161"
                    }
                },
                "required": [
                    "priv_mode",
                    "port"
                ]
            },
            "netconf": {
                "type": "object",
                "properties": {
                    "user": {
                        "type": "string",
                        "minLength": 1,
                        "default": "admin"
                    },
                    "port": {
                        "type": "integer",
                        "maximum": 65535,
                        "minimum": 1024,
                        "exclusiveMaximum": True,
                        "exclusiveMinimum": True
                    }
                },
                "required": [
                    "user",
                    "port"
                ]
            }
        }
    }
}
