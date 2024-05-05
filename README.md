American Sign Language Recognition
============================================================================================

This repository contains my project for the course LT2326 at the Göteborgs Universitet. The repository forked the repository `WLASL` by dxli94 and builds on the work of Li et al. producing the `WLASL` dataset described in "Word-level Deep Sign Language Recognition from Video: A New Large-scale Dataset and Methods Comparison". Following there work, linguistic mistakes in the label sets were changed and the training and testing was repeated. The improvement of the label set was done using the scripts `label_manipulation.py` and `size_check.py`. Those scripts can be found in the folder `code`.

Download Original Videos
-----------------
1. Download repo.
```
git clone https://github.com/dxli94/WLASL.git
```

2. Install [youtube-dl](https://github.com/ytdl-org/youtube-dl) for downloading YouTube videos.
3. Download raw videos.
```
cd start_kit
python video_downloader.py
```
4. Extract video samples from raw videos.
```
python preprocess.py
```
5. You should expect to see video samples under directory ```videos/```.

Requesting Missing / Pre-processed Videos
-----------------

Videos can dissapear over time due to expired urls, so you may find the downloaded videos incomplete. In this regard, Li et al. provide the following solution for you to have access to missing videos.

We also provide pre-processed videos for the full WLASL dataset on request, which saves troubles of video processing for you.

 (a) Run
```
python find_missing.py
```
to generate text file missing.txt containing missing video IDs.

 (b)  Submit a video request by agreeing to terms of use at:  https://docs.google.com/forms/d/e/1FAIpQLSc3yHyAranhpkC9ur_Z-Gu5gS5M0WnKtHV07Vo6eL6nZHzruw/viewform?usp=sf_link. You will get links to the missing videos within 7 days.


Training and Testing
---------------
The training and testing was done two times. Firstly, the training and testing was done in exactly the same way as done by Li et al. following the forked repository. Secondly, the labels were changed and the training and testing was done on the resulting data. Please find descriptions of the procedures below.

**First**


```
cd WLASL
mkdir data
```
put all the videos under ```data/```.
```
cp WLASL2000 -r data/
```
To train models, first download [I3D weights pre-trained Kinetics](https://drive.google.com/file/d/1JgTRHGBRCHyHRT_rAF0fOjnfiFefXkEd/view?usp=sharing) and unzip it. You should see a folder ```I3D/weights/```.

```
python train_i3d.py
```
To test pre-trained models, first download [WLASL pre-trained weights](https://drive.google.com/file/d/1jALimVOB69ifYkeT0Pe297S1z4U3jC48/view?usp=sharing) and unzip it. You should see a folder ```I3D/archived/```.

```
python test_i3d.py
```
By default the script tests WLASL2000. To test other subsets, please change line 264, 270 in ```test_i3d.py``` properly.

A previous release can be found [here](https://drive.google.com/file/d/1vktQxvRHNS9psOQVKx5-dsERlmiYFRXC/view).

**Second**

To improve the data, use the script
```
python label_manipultion.py
```
and then
```
python size_check.py
```

To train the models, use the following script.
```
python train_i3d_alt.py
```
To test the pre-trained models, use the following sript.
```
python test_i3d_alt.py
```
