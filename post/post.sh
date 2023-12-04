# /bin/bash

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"img":"xyz","mask":"xyz"}' \
  http://127.0.0.1:5000/inpaint

