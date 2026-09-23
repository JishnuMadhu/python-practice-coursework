"""
RPG Sound Generator - Creates simple 8-bit style RPG sound effects as .wav files.
Run this script once to generate all sound files, then play them!

No external libraries needed - uses only Python builtins.
"""

import wave
import struct
import math
import os

SAMPLE_RATE = 44100

def save_wav(filename, samples, sample_rate=SAMPLE_RATE):
    """Save samples as a .wav file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with wave.open(filepath, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        for sample in samples:
            clamped = max(-32768, min(32767, int(sample * 32767)))
            wav_file.writeframes(struct.pack('<h', clamped))
    print(f"  Created: {filename}")


def generate_sine(freq, duration, volume=0.5, sample_rate=SAMPLE_RATE):
    """Generate a sine wave tone."""
    samples = []
    num_samples = int(sample_rate * duration)
    for i in range(num_samples):
        t = i / sample_rate
        fade = 1.0
        # Fade out last 20% of duration
        if i > num_samples * 0.8:
            fade = (num_samples - i) / (num_samples * 0.2)
        sample = volume * fade * math.sin(2 * math.pi * freq * t)
        samples.append(sample)
    return samples


def generate_square(freq, duration, volume=0.3, sample_rate=SAMPLE_RATE):
    """Generate a square wave (classic 8-bit sound)."""
    samples = []
    num_samples = int(sample_rate * duration)
    for i in range(num_samples):
        t = i / sample_rate
        fade = 1.0
        if i > num_samples * 0.8:
            fade = (num_samples - i) / (num_samples * 0.2)
        value = 1.0 if math.sin(2 * math.pi * freq * t) >= 0 else -1.0
        samples.append(volume * fade * value)
    return samples


def generate_noise(duration, volume=0.3, sample_rate=SAMPLE_RATE):
    """Generate white noise."""
    import random
    samples = []
    num_samples = int(sample_rate * duration)
    for i in range(num_samples):
        fade = 1.0
        if i > num_samples * 0.7:
            fade = (num_samples - i) / (num_samples * 0.3)
        samples.append(volume * fade * (random.random() * 2 - 1))
    return samples


# =========================================
# SOUND 1: SWORD ATTACK (quick swoosh)
# =========================================
def make_sword_attack():
    samples = []
    duration = 0.2
    num_samples = int(SAMPLE_RATE * duration)
    import random
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        progress = i / num_samples
        # Noise swoosh with descending pitch
        freq = 800 - 600 * progress
        volume = 0.4 * (1 - progress)  # fade out
        noise_part = random.random() * 2 - 1
        tone_part = math.sin(2 * math.pi * freq * t)
        samples.append(volume * (0.6 * noise_part + 0.4 * tone_part))
    save_wav("1_sword_attack.wav", samples)


# =========================================
# SOUND 2: CRITICAL HIT (impact + flash)
# =========================================
def make_critical_hit():
    samples = []
    duration = 0.4
    num_samples = int(SAMPLE_RATE * duration)
    import random
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        progress = i / num_samples
        # Loud impact burst then descending tone
        if progress < 0.15:
            volume = 0.7
            noise = random.random() * 2 - 1
            tone = math.sin(2 * math.pi * 200 * t)
            samples.append(volume * (0.5 * noise + 0.5 * tone))
        else:
            adjusted = (progress - 0.15) / 0.85
            freq = 300 - 200 * adjusted
            volume = 0.5 * (1 - adjusted)
            samples.append(volume * math.sin(2 * math.pi * freq * t))
    save_wav("2_critical_hit.wav", samples)


# =========================================
# SOUND 3: SHIELD BLOCK / DEFEND
# =========================================
def make_shield_block():
    samples = []
    duration = 0.25
    num_samples = int(SAMPLE_RATE * duration)
    import random
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        progress = i / num_samples
        # Metallic clang - two overlapping frequencies
        volume = 0.5 * (1 - progress)
        tone1 = math.sin(2 * math.pi * 800 * t)
        tone2 = math.sin(2 * math.pi * 1200 * t)
        noise = (random.random() * 2 - 1) * 0.15 * (1 - progress)
        samples.append(volume * (0.4 * tone1 + 0.4 * tone2) + noise)
    save_wav("3_shield_block.wav", samples)


# =========================================
# SOUND 4: PLAYER HURT (ouch!)
# =========================================
def make_player_hurt():
    samples = []
    duration = 0.3
    num_samples = int(SAMPLE_RATE * duration)
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        progress = i / num_samples
        # Quick descending buzz
        freq = 400 - 250 * progress
        volume = 0.5 * (1 - progress)
        # Square wave for that retro feel
        value = 1.0 if math.sin(2 * math.pi * freq * t) >= 0 else -1.0
        samples.append(volume * value * 0.35)
    save_wav("4_player_hurt.wav", samples)


# =========================================
# SOUND 5: ENEMY DEATH (descending spiral)
# =========================================
def make_enemy_death():
    samples = []
    duration = 0.6
    num_samples = int(SAMPLE_RATE * duration)
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        progress = i / num_samples
        # Descending warble
        freq = 600 - 500 * progress
        wobble = 30 * math.sin(2 * math.pi * 15 * t)
        volume = 0.4 * (1 - progress * 0.8)
        value = 1.0 if math.sin(2 * math.pi * (freq + wobble) * t) >= 0 else -1.0
        samples.append(volume * value * 0.35)
    save_wav("5_enemy_death.wav", samples)


# =========================================
# SOUND 6: LEVEL UP (triumphant arpeggio)
# =========================================
def make_level_up():
    samples = []
    # C5 - E5 - G5 - C6 arpeggio
    notes = [523, 659, 784, 1047]
    note_duration = 0.15

    for note_freq in notes:
        num_samples = int(SAMPLE_RATE * note_duration)
        for i in range(num_samples):
            t = i / SAMPLE_RATE
            fade = 1.0
            if i > num_samples * 0.7:
                fade = (num_samples - i) / (num_samples * 0.3)
            sample = 0.4 * fade * math.sin(2 * math.pi * note_freq * t)
            # Add a harmonic for richness
            sample += 0.15 * fade * math.sin(2 * math.pi * note_freq * 2 * t)
            samples.append(sample)

    # Hold the last note longer
    hold_duration = 0.4
    num_samples = int(SAMPLE_RATE * hold_duration)
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        fade = 1 - (i / num_samples)
        sample = 0.4 * fade * math.sin(2 * math.pi * 1047 * t)
        sample += 0.15 * fade * math.sin(2 * math.pi * 1047 * 2 * t)
        samples.append(sample)

    save_wav("6_level_up.wav", samples)


# =========================================
# SOUND 7: COIN / GOLD PICKUP
# =========================================
def make_coin_pickup():
    samples = []
    # Two quick high notes
    notes = [(1200, 0.08), (1600, 0.12)]
    for freq, duration in notes:
        num_samples = int(SAMPLE_RATE * duration)
        for i in range(num_samples):
            t = i / SAMPLE_RATE
            fade = 1.0
            if i > num_samples * 0.6:
                fade = (num_samples - i) / (num_samples * 0.4)
            sample = 0.35 * fade * math.sin(2 * math.pi * freq * t)
            samples.append(sample)
    save_wav("7_coin_pickup.wav", samples)


# =========================================
# SOUND 8: MENU SELECT (UI click)
# =========================================
def make_menu_select():
    samples = []
    duration = 0.08
    num_samples = int(SAMPLE_RATE * duration)
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        progress = i / num_samples
        freq = 900
        volume = 0.35 * (1 - progress)
        samples.append(volume * math.sin(2 * math.pi * freq * t))
    save_wav("8_menu_select.wav", samples)


# =========================================
# SOUND 9: VICTORY FANFARE
# =========================================
def make_victory():
    samples = []
    # Short triumphant melody: G4 - C5 - E5 - G5 (hold)
    melody = [
        (392, 0.12),   # G4
        (523, 0.12),   # C5
        (659, 0.12),   # E5
        (784, 0.5),    # G5 (hold)
    ]
    for freq, duration in melody:
        num_samples = int(SAMPLE_RATE * duration)
        for i in range(num_samples):
            t = i / SAMPLE_RATE
            fade = 1.0
            if i > num_samples * 0.75:
                fade = (num_samples - i) / (num_samples * 0.25)
            # Mix sine + square for a richer 8-bit feel
            sine = math.sin(2 * math.pi * freq * t)
            square = 1.0 if sine >= 0 else -1.0
            sample = fade * (0.3 * sine + 0.15 * square)
            # Add octave harmonic
            sample += 0.1 * fade * math.sin(2 * math.pi * freq * 2 * t)
            samples.append(sample)
    save_wav("9_victory_fanfare.wav", samples)


# =========================================
# SOUND 10: GAME OVER
# =========================================
def make_game_over():
    samples = []
    # Sad descending: E4 - D4 - C4 - (low buzz)
    melody = [
        (330, 0.25),   # E4
        (294, 0.25),   # D4
        (262, 0.5),    # C4 (hold, fade)
    ]
    for freq, duration in melody:
        num_samples = int(SAMPLE_RATE * duration)
        for i in range(num_samples):
            t = i / SAMPLE_RATE
            fade = 1.0
            if i > num_samples * 0.7:
                fade = (num_samples - i) / (num_samples * 0.3)
            sample = 0.35 * fade * math.sin(2 * math.pi * freq * t)
            sample += 0.1 * fade * math.sin(2 * math.pi * freq * 0.5 * t)
            samples.append(sample)
    # Low rumble at the end
    rumble_duration = 0.4
    num_samples = int(SAMPLE_RATE * rumble_duration)
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        fade = 1 - (i / num_samples)
        samples.append(0.3 * fade * math.sin(2 * math.pi * 80 * t))
    save_wav("10_game_over.wav", samples)


# =========================================
# GENERATE ALL SOUNDS
# =========================================
if __name__ == "__main__":
    print("\nGenerating RPG Sound Effects...\n")

    make_sword_attack()
    make_critical_hit()
    make_shield_block()
    make_player_hurt()
    make_enemy_death()
    make_level_up()
    make_coin_pickup()
    make_menu_select()
    make_victory()
    make_game_over()

    print("\nDone! All .wav files created in the 'sounds' folder.")
    print("Double-click any .wav file to listen to it!")
