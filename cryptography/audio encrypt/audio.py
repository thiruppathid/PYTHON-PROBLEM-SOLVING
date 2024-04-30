import tkinter as tk
import tkinter.font as font  # Added import for font
import pyperclip
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play


def cipher(lis):
    encrypted_text = ""
    encrypt = []
    for word in lis:
        n = len(word)
        val = key(n)
        for i in range(len(word)):
            encrypted_text += chr((ord(word[i])) + val)
            if len(encrypted_text) == len(word):
                encrypt.append(encrypted_text)
                encrypted_text = ""
    return " ".join(encrypt)

def decrypt(encrypt):
    decrypt = []
    for word in encrypt:
        n = len(word)
        val = key(n)
        decrypt_text = ""  
        for i in range(len(word)):
            decrypt_text += chr(ord(word[i]) - val)
        decrypt.append(decrypt_text)
    return " ".join(decrypt)

def key(n):
    n = n * 2
    n += 2
    n *= 5
    n += 5
    return prime(n)

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(n):
    lower_prime = n - 1
    upper_prime = n + 1
    if not isprime(lower_prime):
        lower_prime = -1
    if not isprime(upper_prime):
        upper_prime += 1
    if abs(n - lower_prime) <= abs(n - upper_prime):
        return lower_prime
    else:
        return upper_prime

def text_to_cipher(plain_text):
    return cipher(plain_text.split())

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return "Error: Could not recognize audio"
    except sr.RequestError as e:
        return f"Error: {e}"

def on_encrypt_button_click():
    plain_text = plain_text_entry.get()
    if plain_text:
        cipher_text = text_to_cipher(plain_text)
        result_label.config(text=f'Cipher Text: {cipher_text}', font=large_font)
        plain_text_entry.delete(0, tk.END)
        encrypt_button.configure(bg='green', font=('Helvetica', 12, 'bold'))

def on_decrypt_button_click():
    cipher_text = cipher_text_entry.get()
    if cipher_text:
        plain_text = decrypt(cipher_text.split())
        result_label.config(text=f'Plain Text: {plain_text}', font=large_font)
        cipher_text_entry.delete(0, tk.END)
        decrypt_button.configure(bg='blue', font=('Helvetica', 12, 'bold'))

def on_copy_button_click():
    result_content = result_label.cget("text")
    pyperclip.copy(result_content)

def on_convert_audio_button_click():
    audio_file_path = audio_file_entry.get()
    if audio_file_path:
        
        text_result = audio_to_text(audio_file_path)
        plain_text_entry.delete(0, tk.END)
        plain_text_entry.insert(0, text_result)

# Create the main window
window = tk.Tk()
window.title("Text to Cipher Text Converter")

# Create and place widgets
plain_text_label = tk.Label(window, text="Enter Plain Text:")
plain_text_label.pack()

plain_text_entry = tk.Entry(window, width=80)
plain_text_entry.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=on_encrypt_button_click)
encrypt_button.pack()

cipher_text_label = tk.Label(window, text="Enter Cipher Text:")
cipher_text_label.pack()

cipher_text_entry = tk.Entry(window, width=80)
cipher_text_entry.pack()

decrypt_button = tk.Button(window, text="Decrypt", command=on_decrypt_button_click)
decrypt_button.pack()

large_font = font.Font(family='Helvetica', size=14)
result_label = tk.Label(window, text="", width=50, font=large_font)
result_label.pack()

copy_button = tk.Button(window, text="Copy Result", command=on_copy_button_click)
copy_button.pack()

# Additional widgets for audio processing
audio_file_label = tk.Label(window, text="Enter Audio File Path:")
audio_file_label.pack()

audio_file_entry = tk.Entry(window, width=80)
audio_file_entry.pack()

convert_audio_button = tk.Button(window, text="Convert Audio", command=on_convert_audio_button_click)
convert_audio_button.pack()

# Run the GUI
window.mainloop()

