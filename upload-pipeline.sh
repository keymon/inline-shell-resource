yes | fly -t hectorshell-bootstrap destroy-pipeline -p test && ssh -F ssh-config default /var/vcap/packages/jettison/bin/jettison && fly -t hectorshell-bootstrap set-pipeline -p test -c examples/test-pipeline.yml

