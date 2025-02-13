## image-scanner

To make image processing like a scanner. Return image in base64. Input in image file 

"file": image_file

### Requirements

- Docker

### Development

To run the project you need to run the following command:

```shell
$ docker-compose up
```

The API will be executed and you will have this available endpoints:

- POST `http://localhost:7070/scan` - Input your image "file": image_file (form-data)

### Deployment

This project can be easily deployed into vercel by just importing the repo, no further configuration needed.

### DEMO

https://image-scanner.vercel.app/