# Project TODO List

## W&B Integration

- [ ] Set up W&B project for ISCR group: [ISCR W&B Project](https://wandb.ai/iscr)

## High-Level Overview

### Images

- **Compound/Continuous Set**
    - [ ] Prepare 2000 images for each letter
        - [ ] 1000 for continuous shapes
        - [ ] 1000 for compound shapes
    - **Total**: 52,000 images

### First Blocker

1. **How to Make Images Compound (Dotted Shapes)**
   - [ ] Gilles to provide dataset for compound letters

### Models

1. **Model Parameters**
    - [ ] Specify if ImageNet Pretrain is required (Y/N)
    - [ ] Define finetuning details (Y/N, dataset, parameters)
    - [ ] Specify mini datasets as needed for the image task

2. **Results**
    - [ ] Save model weights online
    - [ ] Integrate with Weights and Biases for comprehensive tracking

3. **Ablation Testing**
    - [ ] Script for ablating layers (parameters: layer number)
    - [ ] Measure performance metrics after ablating layers

4. **Build Charts**
    - [ ] Create performance charts similar to Paper 1
        - [ ] Human Similarity (Relative Score)
        - [ ] ...

## Experiment 1: Compound vs Continuous Letters

1. **Cognitive Science Concept Derived from Hypothesis**
    - [ ] Define hypothesis related to orientation of letters
    - [ ] Identify cognitive concept for experimentation

2. **Human Experimental Suite / Data**
    - [ ] Obtain experimental data from Davida (5.8/5.9)

3. **Computational Experiment**
    - [ ] Establish relation between DNNs and visual stream
    - [ ] Formulate assumptions related to cognitive concept
    - [ ] Prove cognitive concept using computational experiment

4. **Psychological Representations to Computational Experiment**
    - [ ] Establish connection between psychological and computational experiments

5. **Theory for Experiment**
    - [ ] Refine theory with Gilles
    - [ ] Formulate theories based on human capability and model training

6. **Experiment Details**
    - [ ] Train models on compound and continuous exemplars
    - [ ] Test models on compound/continuous exemplars
    - [ ] Conduct ablative analysis on model layers

## Engineering Methodology

1. **Models Other Than DNNs**
    - **Shallow Models:**
        - [ ] Pixelwise
        - [ ] GaborJet
        - [ ] Histogram of Oriented Gradient
        - [ ] Pyramid Histogram of Oriented Gradient
        - [ ] Pyramid Histogram of Visual Words
    - **HMAX Models:**
        - [ ] HMAX 99’
        - [ ] HMIN
        - [ ] HMAX-PNAS

2. **Deep Models**
    - **Models:**
        - [ ] GoogleLeNet
        - [ ] VGG
        - [ ] ResNet
    - **Image Set:**
        - [ ] Prepare 2000 images for each letter
            - [ ] 1000 for continuous shapes
            - [ ] 1000 for compound shapes
        - **Total**: 52,000 images
    - **Training Decisions:**
        - [ ] Pretrained on ImageNet + finetuned on use case
        - [ ] Fully trained only on use case, no ImageNet weights

3. **Evaluation**
    - [ ] Create bar charts of performance
    - [ ] Conduct ablative testing for each model and layer

