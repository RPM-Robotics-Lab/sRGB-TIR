<h2 align="center">
  Dear ICRA reviewers
  ** Source code will be available soon after review process **
</h2>

# Edge-guided Multi-domain RGB-to-TIR image Translation for Training Vision Tasks with Challenging Labels 
Submitted to ICRA 2023 

<div align="left">  
  <a href="https://scholar.google.com/citations?user=u6VDnlgAAAAJ&hl=ko&oi=ao">Dong-Guw Lee</a>,  
  <a href="https://scholar.google.co.kr/citations?user=ivOqySYAAAAJ">Myung-Hwan Jeon</a>
  <a href="https://scholar.google.com/citations?user=W5MOKWIAAAAJ&hl=ko&oi=ao">Younggun Cho</a>,  
  <a href="https://ayoungk.github.io/">Ayoung Kim</a> at <a href="https://rpm.snu.ac.kr">RPM Robotics Lab</a>
</div>

[overview_new.pdf](https://github.com/rpmsnu/sRGB-TIR/files/9655089/overview_new.pdf)


## Overview of the edge-guided multi-domain RGB2TIR translation network



 - ***PrimA6D (RA-L 2020)***
    - PrimA6D reconstructs the rotation primitive and its associated keypoints corresponding to the target object for enhancing the orientation inference.
    <div align="center">
      <a href="https://www.youtube.com/watch?v=HbNmsmTLRmk"><img src="assets/prima6d.png" width="75%" alt="IMAGE ALT TEXT"></a>
    </div>
    
    - More details in [PrimA6D: Rotational Primitive Reconstruction for Enhanced and Robust 6D Pose Estimation](https://arxiv.org/abs/2006.07789)

 
    
   - With estimated uncertainties, PrimA6D++ handles object ambiguity without prior information on object shape.
   
    <div align="center">
      <a href="https://www.youtube.com/watch?v=akbI61jUJgY"><img src="assets/prima6d++_2.gif" width="49%" alt="IMAGE ALT TEXT"></a>
      <a href="https://www.youtube.com/watch?v=akbI61jUJgY"><img src="assets/prima6d++_4.gif" width="49%" alt="IMAGE ALT TEXT"></a>
    </div>
    
   - More details in [Ambiguity-Aware Multi-Object Pose Optimization for Visually-Assisted Robot Manipulation]()

 - ***Object-SLAM for Multi-Object Pose Optimization (Under Review)***
   - Leveraging the uncertainty, we formulate the problem as an object-SLAM to optimize multi-object poses.
   
    <div align="center">
      <a href="https://www.youtube.com/watch?v=akbI61jUJgY"><img src="assets/slam.gif" width="75%" alt="IMAGE ALT TEXT"></a>      
    </div>   
   
   - More details in [Ambiguity-Aware Multi-Object Pose Optimization for Visually-Assisted Robot Manipulation]()

  
## How to use

 TBA.


## Network Details##


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
