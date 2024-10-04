# Wagtail dhivehi translate

Wagtail Localize offers Machine translations through DeepL and Google Cloud, however for Dhivehi Language in my usecase, google cloud is significantly worse than using claude-sonnet-3.5 for translating dhivehi. So I created this file which is in my project. As of now this is not a package, but hopefully I will get back to this.

![image](https://github.com/user-attachments/assets/c7da6ffa-a5a3-4803-92ea-06a1abff3962)
It is working quite awesomely for me, and the cost is not too high and in the case of dhivehi that is really accurate.

In comparison here is google translate.
![image](https://github.com/user-attachments/assets/0157240b-dd5d-4a5d-b7af-155d5a690c1a)

I feel like sonnet is better, but its not that worse in case of this specefic translation for either options. (Still prefer sonnet)


To be used with wagtail_localize package.

Read this section to understand: https://wagtail-localize.org/stable/how-to/integrations/machine-translation/#custom-integrations

## Usage

1.place the file anywhere you want in your project

2. Add the following to your settings.py

```python
WAGTAILLOCALIZE_MACHINE_TRANSLATOR = {
    "CLASS": "newsadmin.claude_translate.DhivehiTranslate",
}
```

My file is placed inside my django app called `newsadmin` `newsadmin/claude_translate.py`

### TODO

- [ ] Package it
- [ ] Allow multiple languages through options
- [ ] Add openai and other providers and make a base wrapper wrapping around all of them
