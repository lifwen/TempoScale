# TempoScale: A Cloud Workloads Prediction Approach Integrating Short Term and Long Term Information
A work published in 2024 IEEE 17th International Conference on Cloud Computing (CLOUD).

## About
**Introduction of TempoScale:**
* Innovative solution to address cluster dynamics and workload variability.
* Captures correlations in time series data for intelligent elastic scaling.
  
**Key Features:**
* Long-term trend analysis:
  * Reveals changes in workload and resource demands.
  * Supports proactive resource allocation over extended periods.
* Short-term volatility analysis:
  * Examines variations in workload and resource demands.
  * Facilitates real-time scheduling and rapid responsiveness.
    
**Experimental Validation:**
  * Conducted experiments on K8s with realistic data from Alibaba.
  * Results demonstrate feasibility of TempoScale.
    
**Benefits:**
* Enhances system performance and stability.
* Effectively reduces resource costs.
* Promotes sustainable development of cloud computing across various industries.

## Getting Started
* **Auto-Scaling:** It contains our designed auto-scaling algorithm, which can be used for auto-scaling on the K8s.
* **CEEMDAN:** It contains the modal decomposition algorithm in TempoScale.
* **Long-Term:** It contains the Informer algorithm for long-term forecasting in TempoScale.
* **Short-Term:** It contains the esDNN algorithm for short-term forecasting in TempoScale.
* **MLP:** It contains the MLP layer used for processing intermediate results in TempoScale.

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
