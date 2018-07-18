import pytest

import app as lexeme_forms

def test_form2input_basic():
    markup = lexeme_forms.form2input({'advanced': False}, {'example': 'Left [placeholder] right.'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" required> right.'

def test_form2input_advanced():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder"> right.'

def test_form2input_first():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.'}, first=True)
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" autofocus> right.'

def test_form2input_preserve_value():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.', 'value': 'value'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" value="value"> right.'

def test_form2input_escape_value():
    markup = lexeme_forms.form2input({'advanced': True}, {'example': 'Left [placeholder] right.', 'value': '"<>&'})
    assert str(markup) == 'Left <input type="text" name="form_representation" placeholder="placeholder" value="&#34;&lt;&gt;&amp;"> right.'

def test_form2input_invalid():
    with pytest.raises(Exception) as excinfo:
        markup = lexeme_forms.form2input({'advanced': True}, {'example': 'No placeholder.'})
    assert 'missing [placeholder]' in str(excinfo.value)