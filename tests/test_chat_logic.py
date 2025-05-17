import pytest
from services import chat_logic

@pytest.mark.asyncio
async def test_handle_space_query_success(monkeypatch):
    # Mock the HTTP response
    async def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self): pass
            def json(self):
                return {
                    "number": 2,
                    "people": [
                        {"name": "Alice", "craft": "ISS"},
                        {"name": "Bob", "craft": "ISS"}
                    ]
                }
        return MockResponse()
    
    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)
    
    response = await chat_logic.handle_space_query()
    assert "There are 2 people in space" in response
    assert "- Alice (ISS)" in response
    assert "- Bob (ISS)" in response


def test_handle_time_query_format():
    result = chat_logic.handle_time_query()
    assert result.startswith("🕒 The current UTC time is")
    assert "UTC on" in result


def test_handle_joke_request():
    result = chat_logic.handle_joke_request()
    assert result.startswith("😂")
    assert any(joke in result for joke in chat_logic.jokes)


def test_handle_help_request():
    result = chat_logic.handle_help_request()
    assert "You can ask me things like" in result
    assert "- Who is in space" in result


def test_handle_default_echo():
    message = "hello"
    result = chat_logic.handle_default_echo(message)
    assert result == "You said: 'hello'"
