import os
import torchaudio
from pathlib import Path

# Root folder with your wavs: wav/train/, wav/dev/, wav/test/
DATASET_ROOT = Path("./audio/")
OUTPUT_ROOT = Path("uems")
OUTPUT_ROOT.mkdir(exist_ok=True, parents=True)

splits = ["test"]

for split in splits:
    wav_dir = DATASET_ROOT / split
    uem_dir = OUTPUT_ROOT / split
    uem_dir.mkdir(exist_ok=True, parents=True)

    for wav_file in wav_dir.glob("*.wav"):
        uri = wav_file.stem

        try:
            waveform, sample_rate = torchaudio.load(wav_file)
            duration = waveform.shape[1] / sample_rate

            with open(uem_dir / f"{uri}.uem", "w") as f:
                f.write(f"{uri} 1 0.000 {duration:.3f}\n")

            print(f"✅ {uri}.uem ({duration:.2f}s)")

        except Exception as e:
            print(f"❌ Failed to process {wav_file.name}: {e}")
