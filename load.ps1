<# End to end creation of cluster to port-forwarding service for locust 
 # on a kind cluster.
 #>
# create kind cluster
kubectl get nodes
if (!$?) {
    kind create cluster
}

# build the docker image, if there is an issue than exit the scrip
docker build . -t aaronarellano/locust-kind
if (!$?) {
    exit
}
docker push aaronarellano/locust-kind

# deploy manifests to kind cluster 
kubectl apply -k manifests/base
# wait for resources to populate
Start-Sleep -s 5
# validate locust pod is running before port forwarding
Write-Host "Waiting for locust pod to enter running state" -NoNewline
DO {
    $podStatus = kubectl get pods -n locust | findstr Running
    Write-Host "." -NoNewline
}
WHILE (!$podStatus)
Write-Host ""

# port forward after the service is up
kubectl port-forward svc/locust-kind 8089 -n locust
