A simple script which generates macOS app icons from a single PNG file.

# Requirements

- macOS
- iconutil (should be already present in your macOS installation) 
- sips (same here)


# Installation

```shell
pip install .
```


# Usage

## From the shell

Simply point the script to the source PNG file and specify the output
directory. The script automatically adds `.iconset` extension to the
directory if needed.

```shell
make-icons my_icon.png my_great_app
```

And that's it.

## From other scripts

Also, you can generate icons directly from your Python script:

```python
import make_icons

make_icons.make_iconset('my_icon.png', 'my_great_app.iconset')
```
