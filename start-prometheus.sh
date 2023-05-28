#!/bin/bash

sudo kubectl get deployments --namespace=monitoring
sleep 1

sudo kubectl port-forward prometheus-deployment-67cf879cc4-h6ngb 1337:9090 -n monitoring

