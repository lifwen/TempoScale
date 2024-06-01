# TempoScale: A Cloud Workloads Prediction Approach Integrating Short Term and Long Term Information
A work published in 2024 IEEE International Conference on Cloud Computing.

## About
Introduction of TempoScale:

*Innovative solution to address cluster dynamics and workload variability.
*Captures correlations in time series data for intelligent elastic scaling.

Key Features:

Long-term trend analysis:
* Reveals changes in workload and resource demands.
* Supports proactive resource allocation over extended periods.
Short-term volatility analysis:
* Examines variations in workload and resource demands.
* Facilitates real-time scheduling and rapid responsiveness.
* Experimental Validation:

Benefits:

* Enhances system performance and stability.
* Effectively reduces resource costs.
* Promotes sustainable development of cloud computing across various industries.

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
