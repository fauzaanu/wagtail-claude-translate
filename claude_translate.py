import os
from wagtail_localize.machine_translators.base import BaseMachineTranslator
from wagtail_localize.strings import StringValue
import anthropic

class DhivehiTranslate(BaseMachineTranslator):
    display_name = "DHIVEHI AI TRANSLATOR"

    def translate(self, source_locale, target_locale, strings):
        translations = {}
        for string in strings:
            dhivehi_text = string.render_text()
            message = self._get_translation_from_claude(dhivehi_text)
            translated_text = self._extract_translation(message.content[0].text)
            translations[string] = StringValue.from_plaintext(translated_text)
        return translations

    def _get_translation_from_claude(self, dhivehi_text):
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )
        return self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": self._get_prompt(dhivehi_text)
                        }
                    ]
                }
            ]
        )

    def _get_prompt(self, dhivehi_text):
        return f"""You are a Dhivehi-to-English translator. Your task is to accurately translate the given Dhivehi text into English.

Here is the Dhivehi text to translate:
<dhivehi_text>
{dhivehi_text}
</dhivehi_text>

Please follow these steps:
1. Read the Dhivehi text carefully.
2. Translate the text into English, ensuring that you maintain the original meaning and context as closely as possible.
3. Pay attention to any cultural nuances or idiomatic expressions that may require special consideration in the translation.
4. Review your translation to ensure it sounds natural in English while staying true to the original Dhivehi text.

Provide your English translation within <translation> tags. If there are any parts of the text that you're unsure about or that may have multiple interpretations, you can provide a brief explanation within <note> tags after your translation.

Begin your translation now."""

    def _extract_translation(self, response):
        start = response.find("<translation>") + len("<translation>")
        end = response.find("</translation>")
        return response[start:end].strip()

    def can_translate(self, source_locale, target_locale):
        return source_locale.language_code != target_locale.language_code
