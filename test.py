import argostranslate.package
import argostranslate.translate

package_path = r"C:\Users\hureu\Downloads\translate-en_ko-1_1.argosmodel"
argostranslate.package.install_from_path(package_path)

installed_languages = argostranslate.translate.get_installed_languages()
if len(installed_languages) == 0:
    print("⚠️ 설치된 번역 모델이 없습니다.")
else:
    texts = [
        "The objective of our research is to create an agent-based environment within which meeting scheduling can be performed and optimized. This system aims to improve productivity through efficient scheduling.", "Our team is focused on developing AI-based solutions for real-world problems."
    ]

    output_path = r"C:\Users\hureu\Documents\translated_output.txt"
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for idx, source_text in enumerate(texts, 1):
                print("원문:", source_text)
                translated_text = argostranslate.translate.translate(source_text, "en", "ko")
                print("번역:", translated_text)

                f.write("원문: " + source_text + "\n")
                f.write("번역: " + translated_text + "\n\n")

        print(f"\n✅ 모든 문장 처리 완료, 결과가 '{output_path}'에 저장되었습니다.")
    except Exception as e:
        print("❌ 파일 저장 중 오류 발생:", e)

