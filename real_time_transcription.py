
### Dependencies
# pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk


def speech_recognized(event_args):
    result = event_args.result
    if result.reason == speechsdk.ResultReason.RecognizingSpeech:
        print(f"Intermediate result: {result.text}")
    elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Final result: {result.text}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")

def main():
    # Replace with your subscription key and region
    speech_key = 'YOUR_SPEECH_KEY'
    service_region = 'YOUR_SPEECH_SERVICE_REGION'

    # Replace with the full path to your WAV file. Note: This does not work with MP3 files, so you will need to convert them to WAV first.
    wav_file_path = "testvideo.wav"

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language="ar-SA")
    audio_config = speechsdk.audio.AudioConfig(filename=wav_file_path)

    # Create a speech recognizer with the given audio config
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Connect the event handler
    speech_recognizer.recognized.connect(speech_recognized)

    # Start continuous recognition (real-time transcription)
    speech_recognizer.start_continuous_recognition()

    try:
        # Keep the program running to allow real-time transcription
        input("Press Enter to stop...\n")
    except KeyboardInterrupt:
        pass
    finally:
        # Stop recognition when done
        speech_recognizer.stop_continuous_recognition()

if __name__ == "__main__":
    main()
