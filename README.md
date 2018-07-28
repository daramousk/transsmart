# transsmart

> This is a wrapper around the RESTful V2 API of transsmart.com. For more
information and full documentation visit 
https://devdocs.transsmart.com/#\_api\_v2\_documentation

## Install

```
pip install Transsmart-V2
```

## Usage

```
As a library:
`from transsmart.connection import Connection`

`connection = Connection().connect(username, password)`

If the connection fails you will get an error else on success you can go
ahead issuing commands using the active connection object:

`response = connection.Shipment.retrieve(account, reference, **kwargs)`
`response = connection.Rate.calculate(account, **kwargs)`

where `response` is a `requests.Response` object.

Command-line interface:

`$ trassmart $username $password $endpoint $function $args`

Example:

`$ transsmart my_username my_password Shipment retrieve account reference arg1=1 arg2=2`
`$ transsmart my_username my_password Rate calculate account arg1=1 arg2=2 arg3=3`



```

## Contribute

Help us make this library better by opening an issue at:

https://github.com/daramousk/transsmart/issues

or contribute a Pull Request at:

https://github.com/daramousk/transsmart/pulls

## License

Read LICENCE
