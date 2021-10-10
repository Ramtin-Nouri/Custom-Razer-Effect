# Custom-Razer-Effect

Custom Razer Keyboard Effect using OpenRazer.  
Something like the **Static + Reactive** effect but the Reactive is more smooth.

# About
I really missed the feature of [Polychromatic](https://polychromatic.app/) being able to stack multiple effects on top of each other like Razer Synapse in windows. Then I did some quick search and stumbled upon [this script by bluzukk](https://gist.github.com/bluzukk/2f5ce1d21bcafbf6dd70d0b8f95a30f1), which basically . I really liked the idea of having a complete custom approach because what now I could also add the ***Reactive smoothing out*** instead of popping back to normal. This setting isn't even possible in windows. So here we are.

# Prerequisites
- Python3 and pip
- openrazor
- numpy
- pynput

# Usage 
```
python3 RamtinsRazerEffect.py
```  
That's it, lol.

# Config
- "Background": Static Color. Color that is always on.
- "React": Reactive Color. Color that is on if a key was pressed.
- "Length": Duration of Reactive Effect.

KEY_MAPPING: The Keymapping is based on my keyboard. That is an Ornata V2. Some keys may vary for you. For now the Keymapping is hardcoded as a dict in getConfig.py . You might want to change some keys there.

# Known Issues
- Media buttons don't work, but they generally don't work for me
- A few other keys or key combinations don't work