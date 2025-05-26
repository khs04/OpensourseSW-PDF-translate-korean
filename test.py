import argostranslate.package
import argostranslate.translate

package_path = r"C:\Users\hureu\Downloads\translate-en_ko-1_1.argosmodel"

# 모델 설치
argostranslate.package.install_from_path(package_path)

installed_languages = argostranslate.translate.get_installed_languages()
print("설치된 언어 목록:", installed_languages)

if len(installed_languages) == 0:
    print("⚠️ 설치된 번역 모델이 없습니다.")
else:
    source_text = "The objective of our research is to create an agent-based environment within which meeting scheduling can be performed and optimized"
    translated_text = argostranslate.translate.translate(source_text, "en", "ko")
    print("번역 결과:", translated_text)

    # 파일 저장 (오류 확인용)
    try:
        output_path = r"C:\Users\hureu\Documents\translated_output.txt"
        print(f"📝 저장 시도 중... 경로: {output_path}")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_text)
        print("✅ 파일이 성공적으로 저장되었습니다.")
    except Exception as e:
        print("❌ 파일 저장 중 오류 발생:")
        print("    👉", type(e).__name__, "-", e)
