# Text-to-image Generation Tasks

## AttnGAN
### Status
AttnGAN is implemented for the `birds` dataset (but some testing is still required). It will download, train, and generate images using a single command through `mlflow`.

One main task remains to be done before this task is ready for general use: either a guide needs to be created for using AttnGAN with new datasets, or an automated configuration file generator can be implemented. Using AttnGAN on a new dataset involves creating configuration files for training and evaluation that includes model hyperparameters.

### Submodule
The following instructions were tailored for the `AttnGAN` task, but it should work for git submodules in general with minimal changes.

#### Download
To download `ai-platform` with all of its submodules, use:
```
git clone https://github.com/produvia/ai-platform.git --recurse-submodules
```

To only download the `AttnGAN` submodule, use:
```
git submodule update --init -- tasks/computer-vision/image-generation/text-to-image/AttnGAN/ # This pulls the ai-platform version of AttnGAN
```

#### Update
To synchronize all of `ai-platform`'s submodules with their source repositories, use:
```
git submodule update --remote # Updates all submodules.
```
To only synchronize `AttnGAN` with its [repository](https://github.com/mlaradji/AttnGAN), use:
```
git submodule update --remote tasks/computer-vision/image-generation/text-to-image/AttnGAN/
```
This will not push any changes to `ai-platform`. To actually push the changes, use:
```
git add tasks/computer-vision/image-generation/text-to-image/AttnGAN
git commit -m "Synchronized AttnGAN with parent repository"
git push
```

#### Notes
A user can also pull only the submodules that they want (https://stackoverflow.com/a/31471460/9954163):
```
git clone https://github.com/mlaradji/ai-platform.git # This shouldn't download any submodules
cd ai-platform
git submodule update --init -- tasks/computer-vision/image-generation/text-to-image/AttnGAN/ # This pulls the ai-platform version of AttnGAN
```

It is possible to have a separate submodule url for each task. It is also worth noting that a submodule is in a detached HEAD state, and is only a reference to specific commits in the submodule's repo. This means several things:
1. It is possible to have two independent submodules that come from the same repo but are of different versions.
2. Updates to a submodule repo will not be automatically pushed to the main (ai-platform) repo.