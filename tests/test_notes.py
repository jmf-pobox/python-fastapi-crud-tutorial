import json
from typing import Any

import pytest
from starlette.testclient import TestClient

from fastapi_crud_tutorial.db import crud
from fastapi_crud_tutorial.schemas.notes import NoteCreate


def test_read_note(test_app: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    test_data = {"id": 1, "title": "something", "description": "something else"}

    async def mock_get(id: int) -> dict[str, Any] | None:
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/notes/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_note_incorrect_id(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    async def mock_get(id: int) -> dict[str, Any] | None:
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/notes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

    response = test_app.get("/notes/0")
    assert response.status_code == 422


def test_read_all_notes(test_app: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    test_data = [
        {"title": "something", "description": "something else", "id": 1},
        {"title": "someone", "description": "someone else", "id": 2},
    ]

    async def mock_get_all() -> list[dict[str, Any]]:
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/notes")
    assert response.status_code == 200
    assert response.json() == test_data


def test_create_note(test_app: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    test_request_payload = {"title": "something", "description": "something else"}
    test_response_payload = {
        "id": 1,
        "title": "something",
        "description": "something else",
    }

    async def mock_post(payload: NoteCreate) -> int:
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post(
        "/notes/",
        content=json.dumps(test_request_payload),
    )

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app: TestClient) -> None:
    response = test_app.post("/notes/", content=json.dumps({"title": "something"}))
    assert response.status_code == 422

    response = test_app.post(
        "/notes/", content=json.dumps({"title": "1", "description": "2"})
    )
    assert response.status_code == 422


def test_update_note(test_app: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    test_update_data = {"title": "someone", "description": "someone else", "id": 1}

    async def mock_get(id: int) -> dict[str, Any] | None:
        return test_update_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id: int, payload: NoteCreate) -> int:
        return 1

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/notes/1/", content=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
        [999, {"title": "foo", "description": "bar"}, 404],
        [1, {"title": "1", "description": "bar"}, 422],
        [1, {"title": "foo", "description": "1"}, 422],
        [0, {"title": "foo", "description": "bar"}, 422],
    ],
)
def test_update_note_invalid(
    test_app: TestClient,
    monkeypatch: pytest.MonkeyPatch,
    id: int,
    payload: dict[str, Any],
    status_code: int,
) -> None:
    async def mock_get(id: int) -> dict[str, Any] | None:
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.put(
        f"/notes/{id}/",
        content=json.dumps(payload),
    )
    assert response.status_code == status_code


def test_delete_note(test_app: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    test_data = {"title": "someone", "description": "someone else", "id": 1}

    async def mock_get(id: int) -> dict[str, Any] | None:
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id: int) -> int:
        return id

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/notes/1")

    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_note_incorrect_id(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    async def mock_get(id: int) -> dict[str, Any] | None:
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete("/notes/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

    response = test_app.delete("/notes/0/")
    assert response.status_code == 422
