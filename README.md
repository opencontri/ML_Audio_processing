# ML_Audio_processing: This repository contains a  Machine Learning project which is based on Audio Processing.
Building machine learning models to classify, describe, or generate audio typically concerns modeling tasks where the input data are audio samples.

These audio samples are usually represented as time series, where the y-axis measurement is the amplitude of the waveform. The amplitude is usually measured as a function of the change in pressure around the microphone or receiver device that originally picked up the audio. Unless there is metadata associated with your audio samples, these time series signals will often be your only input data for fitting a model.

Looking at the samples below, taken from each of the ten classes in the Urbansound8k dataset, it is clear from an eye test that the waveform itself may not necessarily yield clear class identifying information. Consider the waveforms for the engine_idling, siren, and jackhammer classes — they look quite similar.

It turns out one of the best features to extract from audio waveforms (and digital signals in general) has been around since the 1980’s and is still state-of-the-art: Mel Frequency Cepstral Coefficients (MFCCs), introduced by Davis and Mermelstein in 1980. Below we will go through a technical discussion of how MFCCs are generated and why they are useful in audio analysis. This section is somewhat technical, so before we dive in, let’s define a few key terms pertaining to digital signal processing and audio analysis. We’ll link to wikipedia and additional resources if you’d like to dig even deeper.
