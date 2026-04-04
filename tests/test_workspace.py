from workspace.__main__ import main


def test_main(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert "Python workspace is ready." in captured.out
