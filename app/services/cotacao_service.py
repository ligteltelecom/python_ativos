from flask import jsonify
from flask_jwt_extended import get_jwt_identity
import yfinance as yf
from app.modelos.ativo import Ativo

class CotacaoService:
    
    def get_cotation_yahoo(**ativos):
        try:    
            data = yf.download(list(ativos.keys()), period='1d', progress=False)['Close']
            return data.iloc[0] if (len(ativos.keys()) <= 1) else data
        except Exception as e:
            return jsonify({'messagem': 'Erro ao buscar cotação','status': 'Erro','msgErro': repr(e)}), 500
        
    def calc_rentabilidade(ativo_id):
        try:
            current_user_id = get_jwt_identity()
            ativo = Ativo.query.filter_by(id=ativo_id,user_id=current_user_id).first()
            
            if not ativo:
                return jsonify({'messagem': 'Ativo não encontrado', 'status': 'Erro'}), 404
            
            ativoKeys = {f'{ativo.codigo}.SA': float(ativo.preco)}
            ativo_preco_atual = CotacaoService.get_cotation_yahoo(**ativoKeys).iloc[0];
          
            rentabilidade = ((float(ativo_preco_atual) / float(ativo.preco)) -1)
            return jsonify({
                'ativo': ativo.to_json(),
                'preco_atual': f'{ativo_preco_atual:.2f}',
                'rentabilidade': f'{rentabilidade:.1%}'}), 200
        
        except Exception as e:
            return jsonify({
                'messagem': 'Erro ao calcular rentabilidade','status': 'Erro','msgErro': repr(e)}), 500
            
    def calc_carteira():
         current_user_id = get_jwt_identity()
         ativos = Ativo.query.filter_by(user_id=current_user_id).all()         
         
         if not ativos:
             return jsonify({'messagem': 'Carteira vazia', 'status': 'Erro'}), 404
         
         carteira = {a.codigo + '.SA': round(float(a.preco),2) for a in ativos}
         carteiraValor =  sum(carteira.values()) 
         
         cotation = CotacaoService.get_cotation_yahoo(**carteira) 
         
         carteira_atual = {k:round(float(cotation[k].iloc[0]),2) for k in cotation.columns}
         print(carteira_atual)
                      
         carteiraAtual = round(sum(carteira_atual.values()),2)
         
         rentabilidade = (carteiraAtual / carteiraValor) - 1
         
         info_carteira = {
                'carteira Valor': carteiraValor,
                'carteira Valor Atual': carteiraAtual,
                'rentabilidade': f'{rentabilidade:.1%}'
         }
         
         
         return jsonify(info_carteira), 200
         
        
            