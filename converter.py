# -*- coding: utf-8 -*-
import pydub

sound = pydub.AudioSegment.from_mp3("input.mp3")
sound.export("output.wav", format="wav")
