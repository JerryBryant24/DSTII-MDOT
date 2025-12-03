# DSTII-MDOT

This project hosts the code for implementing the DSTII-MDOT algorithm of the 2025 IEEE Internet of Things Journal paper:
```
Dynamic Spatiotemporal Information Interaction for Multi-drone Object Tracking
![image](https://github.com/JerryBryant24/DSTII-MDOT/blob/main/2.png)

Multi-drone object tracking (MDOT) has emerged as a key enabling technology in Internet of Things (IoT)-based aerial sensing systems. By enabling cross-drone information sharing, collaborative trackers effectively mitigate the limitations of single-view object trackers in handling occlusion and object disappearance. However, most existing methods overlook both the temporal continuity across consecutive frames and the spatial complementarity across heterogeneous drone perspectives, which restricts their robustness and scalability in large-scale IoT scenarios.
To address these issues, this paper proposes a dynamic spatiotemporal information interaction for multi-drone object tracking (DSTII-MDOT). 
First, this paper proposes a dynamic temporal feature aggregation (DTFA) module, which captures object motion variations by exploiting frame-to-frame differences, thereby reinforcing temporal consistency in long-term tracking. Next, a spatial alignment method for cross-modal semantic alignment (CMSA) is proposed. This method ensures the semantic alignment of text-image modalities by leveraging the CLIP large model and employs a multi-head cross-attention mechanism to capture the top-k regions of interest within the search area. This enhances cross-drone collaboration and reduces redundant communications in IoT networks. Finally, a wavelet frequency domain feature refinement (WFDFR) module is proposed to enhance the texture features of the template image, effectively solving the problem of blurred texture features or missing details of the object in complex scenes. Experimental results on the multi-drone dataset MDOT demonstrate that the proposed DSTII-MDOT tracker surpasses existing advanced methods in both success rate and precision, validating the effectiveness and superiority of the proposed method.

[**[Models and Raw Results (Baidu)]**](https://pan.baidu.com/s/11D5LYVzc6mmHYRknH4q0Zg?pwd=7536 提取码: 7536)

### Acknowledgement
The code based on the [PyTracking](https://github.com/visionml/pytracking), [PySOT](https://github.com/STVIR/pysot) , [SiamBAN](https://github.com/hqucv/siamban) ,
[Biformer](https://ieeexplore.ieee.org/document/10203555).
We would like to express our sincere thanks to the contributors.
