# TempoScale: A Cloud Workloads Prediction Approach Integrating Short Term and Long Term Information
A work published in 2024 IEEE International Conference on Cloud Computing.

## About
In order to address the inherent dynamics of clusters and the variability of workloads, we have proposed an innovative solution called TempoScale. It is designed to better capture the correlations in time series data, enabling more intelligent and adaptive elastic scaling decisions. TempoScale utilizes long-term trend analysis to reveal the changes in workload and resource demands, supporting proactive resource allocation over extended periods. Additionally, it employs short-term volatility analysis to examine variations in workload and resource demands, facilitating real-time scheduling and rapid responsiveness. We conducted experiments on top of K8s with realistic data from Alibaba, and the results demonstrate the feasibility of our proposed method. Our approach not only enhances system performance and stability but also effectively reduces resource costs, promoting the sustainable development of cloud computing across various industries.

## Getting Started
* The _Auto-Scaling_ folder contains our designed auto-scaling algorithm, which can be used for auto-scaling on the K8s platform.
* The _CEEMDAN_ folder contains the modal decomposition algorithm.
* The _Long-Term_ folder contains the Informer algorithm for long-term forecasting.
* The _Short-Term_ folder contains the esDNN algorithm for short-term forecasting.
* The _MLP_ folder contains the MLP layer used for processing intermediate results.

## Citation
If you use TempoScale for your research, please cite our paper:

```bibtex
@inproceedings{Wen2024,
  title={TempoScale: A Cloud Workloads Prediction Approach Integrating Short-Term and Long-Term Information},
  author={Linfeng Wen and Minxian Xu and Adel N. Toosi and Kejiang Ye},
  booktitle={2024 IEEE 17th International Conference on Cloud Computing (CLOUD)},
  year={2024}
}
```
