payload="eyJob3RzcG90IjogeyJob3N0bmFtZSI6ICJERVNLOTMyTEstRUxPIiwgIm9zIjogIldJTkRPV1MiLCAib3NfdmVyc2lvbiI6ICIxMCIsICJ0b2tlbiI6ICI0ZjQyMGJhNi03ZjcwLTQ3ODctYjFkNy1hMDM4OGRhNWMzYjAiLCAiaXAiOiAiMTIwLjIxMS4zLjExMSIsICJkb3dubG9hZF9zcGVlZF9tYnBzIjogIjkwIiwgInVwbG9hZF9zcGVlZF9tYnBzIjogIjE1IiwgImhvc3QiOiB7ImNwdV9wZXJjIjogIjQwIiwgInJhbV9wZXJjIjogIjQwIiwgImRpc2tfdXNhZ2VfcGVyYyI6ICI0MCIsICJ0b3BfcHJvY2Vzc2VzIjogW3sibmFtZSI6ICJsdWEuZXhlIiwgImNwdV9wZXJjIjogIjQ1IiwgInJhbV9wZXJjIjogIjQ1IiwgImRpc2tfdXNhZ2VfcGVyYyI6ICI0NSJ9XSwgImNob3Nlbl9wcm9jZXNzZXMiOiBbeyJuYW1lIjogInRlYW12aWV3ZXIuZXhlIiwgImNwdV9wZXJjIjogIjQ1IiwgInJhbV9wZXJjIjogIjQ1IiwgImRpc2tfdXNhZ2VfcGVyYyI6ICI0NSJ9XX19fQ"

generate_post_data()
{
cat <<EOF
{
        "entry_raw": {
                "payload":"${payload}=\n"
        }
}
EOF
}


curl -i -H "Accept: application/json" -H "Content-type: application/json" -X POST --data "$(generate_post_data)" "https://shrouded-spire-06255.herokuapp.com/v1/entry_raws"
