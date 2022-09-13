<h2 align="center">
  Dear ICRA reviewers
  ** Source code will be available soon after review process **
</h2>

# Edge-guided Multi-domain RGB-to-TIR image Translationfor Training Vision Tasks with Challenging Labels 
Submitted to ICRA 2023 

<div align="left">  
  <a href="https://scholar.google.com/citations?user=u6VDnlgAAAAJ&hl=ko&oi=ao">Dong-Guw Lee</a>,  
  <a href="https://scholar.google.co.kr/citations?user=ivOqySYAAAAJ">Myung-Hwan Jeon</a>
  <a href="https://scholar.google.com/citations?user=W5MOKWIAAAAJ&hl=ko&oi=ao">Younggun Cho</a>,  
  <a href="https://ayoungk.github.io/">Ayoung Kim</a> at <a href="https://rpm.snu.ac.kr">RPM Robotics Lab</a>
</div>


## What is PrimA6D?
 - ***PrimA6D (RA-L 2020)***
    - PrimA6D reconstructs the rotation primitive and its associated keypoints corresponding to the target object for enhancing the orientation inference.
    <div align="center">
      <a href="https://www.youtube.com/watch?v=HbNmsmTLRmk"><img src="assets/prima6d.png" width="75%" alt="IMAGE ALT TEXT"></a>
    </div>
    
    - More details in [PrimA6D: Rotational Primitive Reconstruction for Enhanced and Robust 6D Pose Estimation](https://arxiv.org/abs/2006.07789)

 - ***PrimA6D++ (Under Review)***
   - PrimA6D++ estimates three rotation axis primitive images and their associated uncertainties.   
   
    <div align="center">
      <a href="https://www.youtube.com/watch?v=akbI61jUJgY"><img src="assets/prima6d++_1.gif" width="49%" alt="IMAGE ALT TEXT"></a>
      <a href="https://www.youtube.com/watch?v=akbI61jUJgY"><img src="assets/prima6d++_3.gif" width="49%" alt="IMAGE ALT TEXT"></a>
    </div>
    
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
 

## Citation

Please consider citing the paper as:
```
@ARTICLE{jeon-2020-prima6d,
author={Jeon, Myung-Hwan and Kim, Ayoung},
journal={IEEE Robotics and Automation Letters}, 
title={PrimA6D: Rotational Primitive Reconstruction for Enhanced and Robust 6D Pose Estimation}, 
year={2020},
volume={5},
number={3},
pages={4955-4962},
doi={10.1109/LRA.2020.3004322}}

@ARTICLE{jeon-2022-prima6d,
title={Ambiguity-Aware Multi-Object Pose Optimization for Visually-Assisted Robot Manipulation},
author={Myung-Hwan Jeon and Jeongyun Kim and Ayoung Kim},
journal={Under Review}}
```

## Contact
If you have any questions, contact here please
```
myunghwan.jeon@kaist.ac.kr
```
