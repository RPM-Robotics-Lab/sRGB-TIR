<h2 align="center">
  Dear ICRA reviewers
  ** Source code will be available soon after review process **
</h2>

### Edge-guided Multi-domain RGB-to-TIR image Translation for Training Vision Tasks with Challenging Labels 
Submitted to ICRA 2023 

<div align="left">  
  <a href="https://scholar.google.com/citations?user=u6VDnlgAAAAJ&hl=ko&oi=ao">Dong-Guw Lee</a>,  
  <a href="https://scholar.google.co.kr/citations?user=ivOqySYAAAAJ">Myung-Hwan Jeon</a>
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


## How to use

 TBA.


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

## Contact
If you have any questions, contact here please
```
donkeymouse@snu.ac.kr
```
