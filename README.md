# EnableDataPipe

### Part 1: Backend Design

**Background**
* At Enable, being able to process and transform data is core to our product.
* At a high level, this involves developing an end-to-end data processing pipeline that
consists of:
  * Image processing techniques to optimize sample scans
  * Computer vision techniques to segment and cluster cells present in the sample
  * Running statistical analysis including cell frequencies, cell interactions, and more
* The most general requirements involve:
  * The ability to process peta-scale data yearly
  * The ability to migrate data collected on-prem to the cloud for cloud processing
  * The ability to move data through a multi-step data pipeline
  * The ability for scientists to verify outputs and data quality
  * The ability for users to monitor the progress of the data pipeline

High-level Questions
* What are your general, high level design ideas for this?
* What type of components or stages do we have to consider?
* What bottlenecks may we experience? Where?
* What forms of optimization can we perform?
* How can we ensure the end data is understandable and usable for the end-user?
