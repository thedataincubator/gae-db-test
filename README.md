# gae-db-test
A simple repository for GAE DB Testing

## Setup
In order to set this up, we need to install gcloud (with either brew cask or apt-get) and add this to your `.bashrc` file:

```
# GAEPATH
FULL_PATH=`command -v gcloud`
export GCLOUD_PATH="$(dirname "$FULL_PATH")/../"
export GAEPATH="$GCLOUD_PATH/lib/third_party"

# Add G-Cloud to path
if [ -f $GCLOUD_PATH/path.bash.inc ]; then
  source $GCLOUD_PATH/path.bash.inc  # 20ms
fi

if [ -f $GCLOUD_PATH//completion.bash.inc ]; then
  source $GCLOUD_PATH//completion.bash.inc  # 15 ms
fi
```

Like in the bottom of [this bashrc file](https://github.com/tianhuil/dotfiles/blob/73eaf1a4fabf5e8be974f4b30ad67546ae544db8/.bashrc)

This appears to work in both OSX and Ubuntu.
