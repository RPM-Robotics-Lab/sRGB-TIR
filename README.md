# Edge-guided Multi-domain RGB-to-TIR image Translation for Training Vision Tasks with Challenging [Labels](https://arxiv.org/pdf/2301.12689.pdf)
Accepted Proceedings to ICRA 2023 

<div align="left">  
  <a href="https://scholar.google.com/citations?user=u6VDnlgAAAAJ&hl=ko&oi=ao">Dong-Guw Lee</a>,  
  <a href="https://scholar.google.co.kr/citations?user=ivOqySYAAAAJ">Myung-Hwan Jeon</a>,
  <a href="https://scholar.google.com/citations?user=W5MOKWIAAAAJ&hl=ko&oi=ao">Younggun Cho</a>,  
  <a href="https://ayoungk.github.io/">Ayoung Kim</a> at <a href="https://rpm.snu.ac.kr">RPM Robotics Lab</a>
</div>


### Overview of the edge-guided multi-domain RGB2TIR translation network


 <div align="center">
    
  ![overview_new-1](https://user-images.githubusercontent.com/91654037/192519743-d21b8957-176b-44c7-a138-22bbfc79fd7b.png)

 </div>


### Proposed pipeline for training vision tasks with challenging labels

- Our target tasks are deep optical flow estimation and object detection in thermal images.


 <div align="center">
    
 ![proposed_method-1](https://user-images.githubusercontent.com/91654037/192519964-302b09af-c368-4ee3-81c8-7d45a5065561.png)


 </div>



### Results

***Disclaimer***

-The same model was used for both synthetic and real RGB to TIR image translation


-The model was trained on identical datasets (sRGB=GTA, TIR=STheReO)

# Results on synthetic RGB to TIR translation


 <div align="center">
    
 ![synthetic_rgb_original-1](https://user-images.githubusercontent.com/91654037/192520365-aab88340-b02a-4836-a810-a0569585588a.png)
 </div>
 
 
# Results on real RGB to TIR translation

  - model trained on synthetic RGB image was adapted to translate real RGB image to TIR image. 

 <div align="center">
    
 ![real_rgb_translation_pdf-1](https://user-images.githubusercontent.com/91654037/192520440-ca12d290-701d-48f3-bdf9-1c49404bb7fd.png)

 </div>

# Results on thermal optical flow estimation using the proposed method

<div align="center">
 
  ![optical_flow_comparison-1](https://user-images.githubusercontent.com/91654037/192520499-a250d58d-14b1-4ae9-9b33-75e64c568537.png)
 
</div>




## Video demonstration


[![Video Label](http://img.youtube.com/vi/zq8Qh9ygm6w/0.jpg)]([https://youtu.be/uLR1RNqJ1Mw](https://youtu.be/zq8Qh9ygm6w)?t=0s)

https://youtu.be/zq8Qh9ygm6w


## TODO
- [x] Upload inference code
-  Upload style selection code
-  Upload training code for custom data training




## Environment Setup

 - ***Download Repo***   
   ````shell
   $ git clone https://github.com/rpmsnu/sRGB-TIR.git
   ````
   
   
 - ***Docker support***   
   
   To make things alot easier for environmental setup, I have uploaded my docker image on Dockerhub,
   
   please use the following command to get the docker
   ````
   $docker pull donkeymouse/donkeymouse:icra
   ````
   *If there persists any problems, please file an issue!
   
   
## How To Use: RGB to TIR translation
 - ***Inference***  
   ````
   $ python3 inference_batch.py --input_folder {input dir to your RGB images} --output_folder {output dir to store your translated images} --checkpoint {weight_file address} --a2b 0 --seed {your choice} --num_style {number of tir styles to sample} --synchronized --output_only 
   ````
   
   For example, to translate RGB images stored under a folder called "input", and say you want to sample 5 styles, run the following command:
    ````
   $python3 inference_batch.py --input_folder ./input --output_folder ./output --checkpoint ./translation_weights.pt --a2b 0 --seed 1234 --num_style 5 --synchronized --output_only --config configs/tir2rgb_folder.yaml
    ````
   
- ***Network weights***

Please download them from here: [{link to google drive}](https://drive.google.com/file/d/1px5BfenEGXZL_J6EsPwFImai6wfmcrnq/view?usp=sharing)

*If the link doesn't work, please file an issue!




## Network Details


Edge-guided multi-domain RGB2TIR translation architecture

- Network Architecture

  - Content Encoder: single 7x7 conv block + four 4x4 conv block + four residual blocks + Instance Normalization
  - Style Encoder: single 7x7 conv block + four 4x4 conv block + four residual blocks + GAP + FC layers
  - Decoder (Generator): 4x4 conv + residual blocks in encoder-decoder architecture. 2 downsampling layers and reflection padding were used. 
  - Discriminator: four 4x4 convolutions. Leaky relu activations; LSGAN for loss function, reflection padding was used. 



- ***Model codes will be released after the review process has been cleared.***


- Training details

  - Iterations: 60,000
  - batch size = 1
  - weight decay = 0.001
  - Optimizer: Adam with B1 = 0.5, B2= 0.999
  - initial learning rate = 0.0001
  - step learning rate policy 
  - Learning rate decay rate(gamma) = 0.5
  - Input image size= 640 x 400 for both synthetic RGB and thermal images
 - ***Config files will be released after the review process has been cleared***




## Citation

Please consider citing the paper as:
```
@ARTICLE{lee-2023-edgemultiRGB2TIR,
author={Lee, Dong-Guw and Kim, Ayoung},
conference={IEEE International Conference on Robotics and Automation}, 
title={Edge-guided Multi-domain RGB-to-TIR image Translation for Training Vision Tasks with Challenging Labels}, 
year={2023},
status={underreview}

```
Also, a lot of the code has been built on top of MUNIT (ECCV2018), so please go cite their paper as well.  

## Contact
If you have any questions, contact here please
```
donkeymouse@snu.ac.kr
```
