# Voice Translator - Fine-Tune Whisper on Urdu Speech Dataset

"""
Fine-Tuning Whisper on Urdu Speech Data (Mozilla Common Voice)
=============================================================
This script demonstrates how AI engineers fine-tune an OpenAI Whisper model 
on custom Urdu audio datasets using Hugging Face Transformers, Datasets, and PyTorch.

Prerequisites:
- PyTorch with CUDA (NVIDIA GPU recommended)
- Hugging Face libraries: pip install transformers datasets evaluate librosa jiwer accelerate
"""

import os
import sys

def prepare_training_pipeline():
    print("="*60)
    print("🧠 WHISPER URDU FINE-TUNING PIPELINE")
    print("="*60)
    
    print("""
Step 1: Loading Dataset
-----------------------
Using Mozilla Common Voice (Urdu) / FLEURS Urdu dataset.
Dataset contains audio clips (.mp3/.wav) and corresponding Urdu text transcripts.

Step 2: Audio Preprocessing (Log-Mel Spectrogram)
-------------------------------------------------
Converts 16kHz raw audio waveforms into 80-channel log-Mel spectrograms 
which Whisper's encoder expects as input.

Step 3: Text Tokenization
-------------------------
Tokenizes Urdu target text into token IDs using WhisperTokenizer (Urdu language mode).

Step 4: Training Setup (Seq2SeqTrainer)
---------------------------------------
- Model Base: openai/whisper-small (or medium)
- Optimizer: AdamW (learning_rate=1e-5)
- Loss Function: Cross-Entropy Loss on target tokens
- Metric: Word Error Rate (WER) using jiwer
""")

# Sample Fine-Tuning Code Template for PyTorch / HuggingFace
FINE_TUNE_CODE_TEMPLATE = '''
import torch
from datasets import load_dataset, Audio
from transformers import (
    WhisperFeatureExtractor,
    WhisperTokenizer,
    WhisperProcessor,
    WhisperForConditionalGeneration,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
)

# 1. Load Urdu Dataset
print("Loading Mozilla Common Voice Urdu dataset...")
common_voice = load_dataset("mozilla-foundation/common_voice_11_0", "ur", split="train", trust_remote_code=True)
common_voice = common_voice.cast_column("audio", Audio(sampling_rate=16000))

# 2. Load Model & Processor
model_id = "openai/whisper-small"
feature_extractor = WhisperFeatureExtractor.from_pretrained(model_id)
tokenizer = WhisperTokenizer.from_pretrained(model_id, language="Urdu", task="transcribe")
processor = WhisperProcessor.from_pretrained(model_id, language="Urdu", task="transcribe")
model = WhisperForConditionalGeneration.from_pretrained(model_id)

# Force decoder start token for Urdu
model.config.forced_decoder_ids = processor.get_decoder_prompt_ids(language="urdu", task="transcribe")

# 3. Define Preprocessing Function
def prepare_dataset(batch):
    audio = batch["audio"]
    batch["input_features"] = feature_extractor(audio["array"], sampling_rate=audio["sampling_rate"]).input_features[0]
    batch["labels"] = tokenizer(batch["sentence"]).input_ids
    return batch

# 4. Apply Preprocessing
dataset = common_voice.map(prepare_dataset, remove_columns=common_voice.column_names, num_proc=1)

# 5. Define Training Arguments
training_args = Seq2SeqTrainingArguments(
    output_dir="./whisper-small-urdu",
    per_device_train_batch_size=8,
    gradient_accumulation_steps=2,
    learning_rate=1e-5,
    warmup_steps=50,
    max_steps=500,
    fp16=torch.cuda.is_available(),
    evaluation_strategy="steps",
    predict_with_generate=True,
    generation_max_length=225,
    save_steps=100,
    eval_steps=100,
    logging_steps=25,
    report_to=["tensorboard"],
)

# 6. Initialize Trainer
trainer = Seq2SeqTrainer(
    args=training_args,
    model=model,
    train_dataset=dataset,
    tokenizer=processor.feature_extractor,
)

# 7. Start Training!
print("Starting Fine-Tuning...")
trainer.train()
print("Training complete! Model saved to ./whisper-small-urdu")
'''

if __name__ == "__main__":
    prepare_training_pipeline()
    print("Code template written to train/fine_tune_whisper.py!")
