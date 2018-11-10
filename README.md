# MarathonEnvs + Maml-rl

Explority implementation of 
* MarathonEnvs
* ml-agents
* pytorch-maml-rl
* maml-rl


### source versions
* MarathonEnvs
* ml-agents = 0.5.1
* pytorch-maml-rl
* maml-rl

### MarathonEnvsMamlRl
-----
### Install



```
# run pytourch-maml-rl
cd pytorch-maml-rl
python main.py --env-name CartPole-v1 --num-workers 8 --fast-lr 0.1 --max-kl 0.01 --fast-batch-size 20 --meta-batch-size 40 --num-layers 2 --hidden-size 100 --num-batches 1000 --gamma 0.99 --tau 1.0 --cg-damping 1e-5 --ls-max-steps 15 --output-folder maml-halfcheetah-dir
```