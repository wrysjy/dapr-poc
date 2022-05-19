# Deploy on Kubernetes
Install Dapr on Kubernetes:
```
dapr init -k
```

Install Redis with Helm:
``` 
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install redis bitnami/redis
```

Run kubectl apply -f <FILENAME> :
```
kubectl apply -f ./deploy/components/statestore.yaml
kubectl apply -f ./deploy/components/pubsub.yaml
kubectl apply -f ./deploy/components/binding.yaml
kubectl apply -f ./deploy/components/configredis.yaml
kubectl apply -f ./deploy/components/subscription.yaml
```

Create docker registry secret:
```
kubectl create secret docker-registry docker-registry-secret --docker-server=<REGISTRY_URL> --docker-username=<USERNAME> --docker-password=<PASSWORD> --docker-email=<EMAIL>
```
 
Deploy application:
``` 
kubectl apply -f ./apps/python.yaml
kubectl apply -f ./apps/nodeapp.yaml
kubectl apply -f ./apps/python-flask.yaml
```