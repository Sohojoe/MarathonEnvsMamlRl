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
* Install the enviroments from (here)[https://github.com/Sohojoe/MarathonEnvsBaselines/releases/tag/v1.0.0]


### Note
* **maml-rl** - I've not been able to get this code to run
* **pytorch-maml-rl** - in progress. Currently testing with the hopper enviroment. I've not figured out how to pass the task to Unity for Unity to score. Right now i'm trying to see if i can get it training


```
# to run pytourch-maml-rl on MacOS (no gpu)
python pytorch-maml-rl/main.py --env-name MarathonAntVel-v0 --num-workers 8 --fast-lr 0.1 --max-kl 0.01 --fast-batch-size 20 --meta-batch-size 40 --num-layers 2 --hidden-size 100 --num-batches 1000 --gamma 0.99 --tau 1.0 --cg-damping 1e-5 --ls-max-steps 15 --output-folder maml-test-dir-004

# windows with gpu
python pytorch-maml-rl\main.py --env-name MarathonAntVel-v0 --num-workers 8 --fast-lr 0.1 --max-kl 0.01 --fast-batch-size 20 --meta-batch-size 40 --num-layers 2 --hidden-size 100 --num-batches 1000 --gamma 0.99 --tau 1.0 --cg-damping 1e-5 --ls-max-steps 15 --output-folder --device cuda maml-test-dir-004

# dev - need to play around with the hyper params
python main.py --env-name Bandit-K5-v0 --num-workers 8 --fast-lr 0.1 --max-kl 0.01 --fast-batch-size 20 --meta-batch-size 40 --num-layers 2 --hidden-size 100 --num-batches 1000 --gamma 0.99 --tau 1.0 --cg-damping 1e-5 --ls-max-steps 15 --output-folder maml-test-dir

python main.py --env-name 2DNavigation-v0 --num-workers 8 --fast-lr 0.1 --max-kl 0.01 --fast-batch-size 20 --meta-batch-size 40 --num-layers 2 --hidden-size 100 --num-batches 1000 --gamma 0.99 --tau 1.0 --cg-damping 1e-5 --ls-max-steps 15 --output-folder maml-test-dir-002

```